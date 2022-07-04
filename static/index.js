
  // Get the modal
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  var captionText = document.getElementById("caption");
  
  // Get the image and insert it inside the modal - use its "alt" text as a caption
  
  
  var vBtn = document.querySelectorAll("#view_btn");
  for(var i = 0; i < vBtn.length; i++)
  {
    vBtn[i].onclick = function(){
      var img = document.getElementById(this.name);
      modal.style.display = "block";
      modalImg.src = img.src;
      captionText.innerHTML = img.alt;
    }

  }
  
  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];
  
  // When the user clicks on <span> (x), close the modal
  span.onclick = function() { 
    modal.style.display = "none";
  }
  
  
  var modalEdit = document.getElementById("editOption");

  var eBtn = document.querySelectorAll("#edit_btn");
  for(var i = 0; i < eBtn.length; i++)
  {
    eBtn[i].onclick = function(){
      modalEdit.style.display = "block";
    }
  }

  var span = document.getElementsByClassName("close")[1];
  
  // When the user clicks on <span> (x), close the modal
  span.onclick = function() { 
    modalEdit.style.display = "none";
  }