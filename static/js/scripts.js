// $("form[name=signup_form").submit(function(e){
//     var $form = $(this);
//     var $error = $form.find(".error");
//     // get data from the form and convert to json format to send it to the back
//     var data = $form.serialize(); 
//     console.log(data)
//     //we send this data with ajax
//     $.ajax({
//         url: "/registration/",
//         type: "POST",
//         data: data,
//         dataType: "json",
//         success: function(resp){
//                     window.location.href = "/profile";
//                 },
//         error: function(resp){
//                     console.log(resp);
//                     // diplay the error message sended from backend
//                     $error.text(resp.responseJSON.error).removeClass('erro--hidden');
//                 }
//     })
//     e.preventDefault();
// }
// );

// $("form[name=login_form").submit(function(e){
//     var $form = $(this);
//     var $error = $form.find(".error");
//     // get data from the form and convert to json format to send it to the back
//     var data = $form.serialize(); 
//     console.log(data)
//     //we send this data with ajax
//     $.ajax({
//         url: "/login/",
//         type: "POST",
//         data: data,
//         dataType: "json",
//         success: function(resp){
//                     // After a user log in we redirect hom to the list-users 
//                     window.location.href = "/list-users";

//                 },
//         error: function(resp){
//                     // diplay the error message sended from backend
//                     $error.text(resp.responseJSON.error).removeClass('erro--hidden');
//                 }
//     })
//     e.preventDefault();
// }
// );