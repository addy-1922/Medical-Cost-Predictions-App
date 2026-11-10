// Small client-side enhancement: focus the first field when the page loads.
document.addEventListener("DOMContentLoaded", () => {
    const firstInput = document.querySelector("input[name='age']");
    if (firstInput) firstInput.focus();
});
