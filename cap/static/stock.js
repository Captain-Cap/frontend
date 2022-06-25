$(function(){
    $('#deleteBalloonModal').on('show.bs.modal', function(e) {
        console.log(e.relatedTarget);

        //get data-id attribute of the clicked element
        let balloonId = $(e.relatedTarget).data('balloon-id');
        let balloonInfo = $(e.relatedTarget).data('balloon-info');

        $(e.currentTarget).find('input[name="uid"]').val(balloonId);

        $('#deleteBalloonInfo').text(balloonInfo);
    });
});
