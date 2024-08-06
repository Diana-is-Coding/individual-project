# individual-project: Inventory Management
Welcome to the **Inventory Management** project repository! My final project with Code Institute - built with Django

This project is designed to help manage an inventory of food and medications. It also includes features to add food items from the inventory to a shopping list. This project serves as a base for building additional features such as an NFC scanner, budgeting, recipe searches, and reminders.

<br />
<!-- Logo -->
<h3 align="center">Purple Haze Inventory README</h3>
<div align="center">
  <a href="https://individual-project-l6gj.onrender.com">
    <img src="static/media/README/logo.png" alt="Logo" width="80" height="80">
  </a>

<!-- Table of Contents -->
<h3 align="left">Table of Contents</h3>
<details>
  <ol>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>  
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ABOUT THE PROJECT -->
## Project Overview

This project is aimed at managing food and medication inventory effectively. Users can add items to the inventory, create shopping lists from the inventory, and perform various other management tasks.


### Pictures
<img src="static/media/README/phone_view.PNG" alt="Over View Picture" width="100" height="100">


## Features

- **User Management**: Create and manage user accounts.
- **Inventory Management**: Add, delete, and categorize items in the inventory.
- **Shopping List**: Add items from the inventory to a shopping list, view, and clear the shopping list.
- **Future Enhancements**:
  - NFC Scanner integration.
  - Budgeting feature.
  - Recipe search functionality.
  - Reminders for inventory and shopping lists.

### Pictures
<img src="static/media/README/registration page before CSS.PNG" alt="Feature" width="100" height="100">
<img src="static/media/README/userprofile update form.PNG" alt="Feature" width="100" height="100">
<img src="static/media/README/dashboards.PNG" alt="Feature" width="100" height="100">
<img src="static/media/README/phone_view.PNG" alt="Feature" width="100" height="100">


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/Diana-is-Coding/individual-project.git
    ```

2. Navigate to the project directory:
    ```
    cd individual-project
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```
    python manage.py migrate
    ```

5. Create a superuser account:
    ```
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```
    python manage.py runserver
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- USAGE EXAMPLES -->
## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`. 

### Pictures

![Usage](path/to/usage_image.png)  <!-- Add your usage image here -->

- **Register**: Create a new user account.


- **Login**: Log in to your account.


- **Inventory Management**: Add, delete, and view items in the inventory.


- **Shopping List**: Add items from the inventory to your shopping list and manage the list.



<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please reach out to Diana via:

- Email: [dt.lab1991@gmail.com](mailto:dt.lab1991@gmail.com)
- GitHub: [Diana-is-Coding](https://github.com/Diana-is-Coding)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

<p align="right">(<a href="#readme-top">back to top</a>)</p>