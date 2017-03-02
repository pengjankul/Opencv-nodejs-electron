// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.
// var fs = require('fs')
var remote = require('electron').remote
// var contents = fs.readFileSync('./package.json','utf8')
// alert(contents)
window.onload = function() {

     $("#display-form").show(); //hide form 
    const selectDirBtn = document.getElementById('add')
    const selectRange = document.getElementById('rangeInput')


    const selectImage1 = document.getElementById('images-show1')
    const selectImage2 = document.getElementById('images-show2')
    const selectImage3 = document.getElementById('images-show3')
    const selectImage4 = document.getElementById('images-show4')

    selectDirBtn.addEventListener('change', function (event) {

        if (selectDirBtn.checked){
            var spawn  = require('child_process').spawn
            var process = spawn('python', ['./facedetection.py',selectRange.value]);

            process.stdout.on('data', function (data){
                // Do something with the data returned from python script
                //  $("#display-form").show();
          
               remote.getCurrentWindow().reload();

               $('#add').prop('checked', false);
            
            });
        }
    })




    selectImage1.addEventListener('click', function (event) {
        const value = selectImage1.src;
        const paths = value.split('/')
        const path = paths[paths.length-1]

        if (path){
            var spawn  = require('child_process').spawn
            var process = spawn('python', ['./merge.py',path]);

            process.stdout.on('data', function (data){
                // Do something with the data returned from python script
                //  $("#display-form").show();
             //   remote.getCurrentWindow().reload();
               $("#result-image").attr('src',"img_result0.png");
             
            });
        }
    })

    selectImage2.addEventListener('click', function (event) {
        const value = selectImage2.src;
        const paths = value.split('/')
        const path = paths[paths.length-1]

        if (path){
            var spawn  = require('child_process').spawn
            var process = spawn('python', ['./merge.py',path]);

            process.stdout.on('data', function (data){
                // Do something with the data returned from python script
                //  $("#display-form").show();
           //     remote.getCurrentWindow().reload();
               $("#result-image").attr('src',"img_result1.png");
            });
        }
    })

    selectImage3.addEventListener('click', function (event) {
        const value = selectImage3.src;
        const paths = value.split('/')
        const path = paths[paths.length-1]

        if (path){
            var spawn  = require('child_process').spawn
            var process = spawn('python', ['./merge.py',path]);

            process.stdout.on('data', function (data){
                // Do something with the data returned from python script
                //  $("#display-form").show();
             //   remote.getCurrentWindow().reload();
               $("#result-image").attr('src',"img_result2.png");
            });
        }
    })

    selectImage4.addEventListener('click', function (event) {
        const value = selectImage4.src;
        const paths = value.split('/')
        const path = paths[paths.length-1]

        if (path){
            var spawn  = require('child_process').spawn
            var process = spawn('python', ['./merge.py',path]);

            process.stdout.on('data', function (data){
                // Do something with the data returned from python script
                //  $("#display-form").show();
                //remote.getCurrentWindow().reload();
               $("#result-image").attr('src',"img_result3.png");
            });
        }
    })






    
};



