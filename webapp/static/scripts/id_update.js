let information_list = document.querySelectorAll(".information");
const regex = /\s/g;
information_list.forEach((obj)=>{
  obj.id = obj.id.replace(regex, "+");
});