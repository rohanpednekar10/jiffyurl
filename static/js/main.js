function copyLink() {
  /* Get the text field */
  var copyURL = document.getElementById("short-url");

  /* Select the text field */
  copyURL.select();
  copyURL.setSelectionRange(0, 2000); /*For mobile devices*/

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert the copied text */
  alert("Copied the URL: " + copyURL.value);
}