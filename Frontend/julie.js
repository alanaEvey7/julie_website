/*
var Email = localStorage.getItem("Email");
if (Email == null || Email == "") {
    $(document).ready(function () {
        document.write("The page does not exist");
    });
} else {

    $(document).ready(function () {
       
    
    });
}
*/

var makePostRequest = function(url, data, onSuccess, onFailure) {
        $.ajax({
            type: 'POST',
            url: apiUrl + url,
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: "json",
            success: onSuccess,
            error: onFailure
        });
    };

var makeGetRequest = function(url, onSuccess, onFailure) {
       $.ajax({
           type: 'GET',
           url: apiUrl + url,
           dataType: "json",
           success: onSuccess,
           error: onFailure
       });
   };

var makeDeleteRequest = function (url, onSuccess, onFailure) {
        $.ajax({
            type: 'DELETE',
            url: apiUrl + url,
            success: onSuccess,
            error: onFailure
        });
    };


function Logout() 
{
alert("All changes are saved!");
window.location.href = "./LogIn.html";
};

function on_addOrder()
{
    //used in the form for adding an order to the list
    //need to update the Order and Customer tables
    // need to generate an order number
}

