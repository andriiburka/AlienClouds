
// PLACEHOLDERS
//
const form_fields = document.getElementsByTagName('input');

form_fields[1].placeholder = 'Username:';
form_fields[2].placeholder = 'Password:';
form_fields[3].placeholder = 'Repeat password';

// form_fields[1].placeholder = 'Username';
// form_fields[2].placeholder = 'First name';
// form_fields[3].placeholder = 'Last name';
// form_fields[4].placeholder = 'Email';
// form_fields[5].placeholder = 'Password';
// form_fields[6].placeholder = 'Repeat password';

for (const field in form_fields) {
    form_fields[field].className += ' form-control'
}
