document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch locations and populate the dropdown
    async function populateLocations() {
        try {
            const response = await fetch('/get_location_names');
            const data = await response.json();
            const locationDropdown = document.getElementById('location');

            if (data.locations) {
                data.locations.forEach(location => {
                    const option = document.createElement('option');
                    option.value = location;
                    option.textContent = location;
                    locationDropdown.appendChild(option);
                });
            }
        } catch (error) {
            console.error('Error fetching locations:', error);
        }
    }

    // Call the function to populate locations
    populateLocations();

    // Function to handle button clicks for BHK and Bath
    function handleButtonClick(event) {
        const buttons = event.target.parentElement.querySelectorAll('button');
        buttons.forEach(button => button.classList.remove('active'));
        event.target.classList.add('active');
    }

    // Add event listeners to BHK and Bath buttons
    const bhkButtons = document.querySelectorAll('.bhk-btn');
    const bathButtons = document.querySelectorAll('.bath-btn');

    bhkButtons.forEach(button => button.addEventListener('click', handleButtonClick));
    bathButtons.forEach(button => button.addEventListener('click', handleButtonClick));

    // Function to handle the "Estimate Price" button click
    document.querySelector('.estimate-btn').addEventListener('click', async function () {
        const area = document.getElementById('area').value;
        const bhk = document.querySelector('.bhk-btn.active').getAttribute('data-bhk');
        const bath = document.querySelector('.bath-btn.active').getAttribute('data-bath');
        const location = document.getElementById('location').value;

        if (!area || !location || !bhk || !bath) {
            alert('Please fill in all the fields.');
            return;
        }

        const requestData = {
            total_sqft: parseFloat(area),
            location: location,
            bhk: parseInt(bhk),
            bath: parseInt(bath)
        };

        try {
            const response = await fetch('/predict_home_price', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            });

            const data = await response.json();
            if (data.estimated_price) {
                document.querySelector('.result').textContent = `Estimated Price: ₹${data.estimated_price} Lakhs`;
            } else {
                document.querySelector('.result').textContent = 'Error estimating price.';
            }
        } catch (error) {
            console.error('Error estimating price:', error);
            document.querySelector('.result').textContent = 'Error estimating price.';
        }
    });
});