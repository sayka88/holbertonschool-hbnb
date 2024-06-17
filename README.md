# HBnB Evolution Project

## Overview

Welcome to the HBnB Evolution project, a web application modeled after AirBnB using Python and Flask. This project is designed to teach foundational web development concepts and practices.

## Project Structure

The project is divided into three main layers:

1. **Services Layer**: Handles API requests and responses.
2. **Business Logic Layer**: Processes and makes decisions based on the application's logic.
3. **Persistence Layer**: Manages data storage (currently file-based, moving to a database in the future).

### Key Entities

- **Places**: Representing rental locations with various attributes like name, description, address, etc.
- **Users**: Owners (hosts) or reviewers with attributes like email, password, first name, and last name.
- **Reviews**: User feedback and ratings for places.
- **Amenities**: Features of places such as Wi-Fi, pools, etc.
- **Country and City**: Each place is tied to a city, and each city belongs to a country.

### Business Logic Rules

- Unique Users: Each user is identified by a unique email.
- One Host per Place: Every place must have exactly one host.
- Flexible Hosting: A user can host multiple places or none.
- Open Reviewing: Users can write reviews for places they don’t own.
- Amenity Options: Places can have multiple amenities from a catalog, and users can add new ones.
- City-Country Structure: A place belongs to a city, and each city belongs to a country.

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system.
- `pip` package manager.

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sayka88/holbertonschool-hbnb.git
    cd holbertonschool-hbnb
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

1. **Ensure you are in the root directory of the project**.
2. **Run the tests**:
    ```bash
    python3 -m unittest discover tests
    ```

You should see output similar to this:
..........
Ran 10 tests in 1.002s

OK


## Future Work

- Transition to database storage.
- Implement additional features and entities.
- Enhance the API with more endpoints and functionality.

## Contributing

Contributions are welcome! Please create a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.

## Authors

- Farhad Asgarzada
- Sayyara Yusupova
- Kanan Shafizada
