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
  
  // -----------------------------------------------------------------------------------------------


  // var modalEdit = document.querySelectorAll("#editOption");
  // console.log(modalEdit);
  // var captionEdit = document.getElementById("editCaption");
  // var imgEdit = document.getElementById("imgSource");

  
  var eBtn = document.querySelectorAll("#edit_btn");
  for(var i = 0; i < eBtn.length; i++)
  {
    eBtn[i].onclick = function(){

      var completeId = "editOption"+this.name;
      var modalEdit = document.getElementById(completeId);
      modalEdit.style.display = "block";

      // var imageId = "editImg"+this.name;
      // var imgEdit = document.getElementById(imageId);
      // imgEdit.src = 
      
      var crossId = "closeEdit" + this.name;
      var cross = document.getElementById(crossId);
      cross.onclick = function(){
        modalEdit.style.display = "none";
      }


      // var parentChild = "#"+ completeId + " .closeEdit";
      // console.log (parentChild);
      // var cross = document.querySelector(parentChild);
      // console.log(cross);
      // cross.onclick = function(){
      //   modalEdit.style.display = "none";
      // }

    }
    // var span2 = document.getElementsByClassName("closeEdit")[i];
    // console.log(span2);
    // span2.onclick = function() { 
    //   modalEdit.style.display = "none";
    // }
  }

  // var span2 = document.querySelector( .closeEdit);
  // // console.log(span2);
  
  // // When the user clicks on <span> (x), close the modal
  // span2.onclick = function() { 
  //   globalCross.style.display = "none";
  // }