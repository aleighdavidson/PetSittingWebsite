function redirectUser(id){
window.location.href = 'http://127.0.0.1:5000/edituser/'+ id;
}

function redirectDog(id){
window.location.href ='http://127.0.0.1:5000/editdog/'+ id;
}

function redirectCancel(id){
window.location.href ='http://127.0.0.1:5000/account/'+ id;
}

function removeDog(id){
service.remove_dog(id)}

// Switches buttons between sitter and owner (finish Account Page) //
function switchTab(value) {
var sitterSwitch = document.getElementById("tabswitchSitter");
var ownerSwitch = document.getElementById("tabswitchOwner");
if (value === 'SitterTab') {
    if (sitterSwitch.classList.contains('selectedTab')) {
        return;
    }
    ownerSwitch.classList.remove('selectedTab');
    sitterSwitch.classList.add('selectedTab');

    document.getElementById("OwnerTab").hidden = true
    document.getElementById("SitterTab").hidden = false;
}
if (value === 'OwnerTab') {
    if (ownerSwitch.classList.contains('selectedTab')) {
        return;
    }
    sitterSwitch.classList.remove('selectedTab');
    ownerSwitch.classList.add('selectedTab');

    document.getElementById("SitterTab").hidden = true
    document.getElementById("OwnerTab").hidden = false;
}
}

// Displays images when chosen from file (finish Account Page)//
function showImages(){
    listOfPics = document.getElementById('profilePictures').files
    imageDiv = document.getElementById('imagePreviewContainer')
    imageDiv.innerHTML = ''

    for (var i = 0; i < listOfPics.length; i++) {
        var createdImg = document.createElement("img")
        createdImg.height = "200"
        createdImg.width = "200"
        createdImg.src = URL.createObjectURL(listOfPics[i])
        imageDiv.appendChild(createdImg)
    }
}


// for login //
function tryLogin() {
    emailVar = document.getElementById('emailInput').value;
    passwordVar  = document.getElementById('passwordInput').value;
    window.location.href = '/login?' + emailVar + '?' + passwordVar;
}


