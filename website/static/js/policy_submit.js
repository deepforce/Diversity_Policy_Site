$(function(){
    if ( $('[type="date"]').prop('type') != 'date' ) {
        $('[type="date"]').datepicker({ dateFormat: 'yy-m-d', minDate: 0 }).change(evt => {
            $('.dateerror').remove();
          }).change(function() {
            var now = moment().startOf('day');
            var selectedDate = $(this).datepicker('getDate');
            if (selectedDate < now) {
                $(this).after('<span class="dateerror error" style="color:red">Please enter a valid date (YYYY-MM-DD)</span>');
                $('#request').submit(function(e){
                    if($('.dateerror').length > 0) {
                        e.preventDefault();
                    }
                });
            } else if(!moment($(this).val(), 'YYYY-M-D', true).isValid()) {
                $(this).after('<span class="dateerror error" style="color:red">Please enter a valid date (YYYY-MM-DD)</span>');
                $('#request').submit(function(e){
                    if($('.dateerror').length > 0) {
                        e.preventDefault();
                    }
                });
            } else {
                $(".dateerror").remove();
            }
         });
    } else {
        $('input[type="date"]').attr('type','text');
        $('#datepicker [type="text"]').datepicker({ dateFormat: 'yy-m-d', minDate: 0 }).change(evt => {
            $('.dateerror').remove();
          }).change(function() {
            var now = moment().startOf('day');
            var selectedDate = $(this).datepicker('getDate');
            if (selectedDate < now) {
                $(this).after('<span class="dateerror error" style="color:red">Please enter a valid date (YYYY-MM-DD)</span>');
                $('#request').submit(function(e){
                    if($('.dateerror').length > 0) {
                        e.preventDefault();
                    }
                });
            } else if(!moment($(this).val(), 'YYYY-M-D', true).isValid()) {
                $(this).after('<span class="dateerror error" style="color:red">Please enter a valid date (YYYY-MM-DD)</span>');
                $('#request').submit(function(e){
                    if($('.dateerror').length > 0) {
                        e.preventDefault();
                    }
                });
            } else {
                $(".dateerror").remove();
            }
         });
    }
});