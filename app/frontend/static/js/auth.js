function switchForm() {
    const registrationForm = document.getElementById("registration-form");
    const loginForm = document.getElementById("login-form");

    if (registrationForm.style.display === "none") {
        registrationForm.style.display = "block";
        loginForm.style.display = "none";
    } else {
        registrationForm.style.display = "none";
        loginForm.style.display = "block";
    }
}

async function sendRequest(url, data) {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            open("/dashboard","_self")
        } else {
            alert("Request failed!");
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

function validateRegistrationForm(event) {
    event.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Add your validation logic here
    if (!name || !email || !password) {
        alert("Please fill in all fields.");
        return;
    }

    if (!validateEmail(email)) {
        alert("Please enter a valid email address.");
        return;
    }

    const registrationData = {
        name,
        email,
        password,
    };

    sendRequest("/api/register", registrationData);
}

function validateLoginForm(event) {
    event.preventDefault();
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    // Add your validation logic here
    if (!email || !password) {
        alert("Please fill in all fields.");
        return;
    }

    if (!validateEmail(email)) {
        alert("Please enter a valid email address.");
        return;
    }

    const loginData = {
        email,
        password,
    };

    sendRequest("/api/login", loginData);
}

function validateEmail(email) {
    // Regular expression to validate email format
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}
