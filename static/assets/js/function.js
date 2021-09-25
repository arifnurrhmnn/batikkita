function readFile(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            var htmlPreview =
                '<img class="img-review" src="' + e.target.result + '" />' +
                '<br>' + input.files[0].name;
            // var wrapperZone = $(input).parent();
            // var previewZone = $(input).parent().parent().find('.preview-zone');
            var boxZone = $(input).parent().parent().find('.preview-zone').find('.box').find('.box-body');

            // wrapperZone.removeClass('dragover');
            // previewZone.removeClass('hidden');
            $('#dropzone-desc').css('display', 'none');
            boxZone.empty();
            boxZone.append(htmlPreview);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$(".dropzone").change(function() {
    readFile(this);
});

// $('#dropzone').on('dragover', function (event) {
//     event.preventDefault();
//     event.stopPropagation();
//     $('#preview-zone').css('display', 'block');
//     $('#dropzone-desc').css('display', 'none');
//     // $(this).addClass('dragover');
// });

// jQuery('#dropzone').on('dragleave', function (event) {
//     event.preventDefault();
//     event.stopPropagation();
//     $('#preview-zone').css('display', 'none');
//     $('#dropzone-desc').css('display', 'block');
//     // $(this).removeClass('dragover');
// });


