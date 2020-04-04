$(document).ready(function(){

    // Show calendar when clicking on date of publication input field
    if ( $('[type="date"]').prop('type') != 'date' ) { // for Safari/browsers that don't support input type "date"
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

    // Author & dept. admin name validation
    $('#first_name').blur(function() {
        if (!/^[a-zA-Z ]+$/.test(this.value) && this.value.length > 0 && $('.fn-error').length == 0){
            $(this).after('<span class="text-danger fn-error error">Please enter a valid name</span>');
        } else if(/^[a-zA-Z ]+$/.test(this.value) && $('.fn-error').length > 0 || this.value.length == 0){
            $('.fn-error').remove();
        }
    });
    
    $('#admin_first_name').blur(function() {
        if (!/^[a-zA-Z ]+$/.test(this.value) && this.value.length > 0 && $('.fn-error').length == 0){
            $(this).after('<span class="text-danger a-fn-error error">Please enter a valid name</span>');
        } else if(/^[a-zA-Z ]+$/.test(this.value) && $('.a-fn-error').length > 0 || this.value.length == 0){
            $('.a-fn-error').remove();
        }
    });

    $('#middle_name').blur(function() {
        if (!/^[a-zA-Z ]+$/.test(this.value) && this.value.length > 0 && $('.mid-error').length == 0){
            $(this).after('<span class="text-danger mid-error error">Please enter a valid name</span>');
        } else if(/^[a-zA-Z ]+$/.test(this.value) && $('.mid-error').length > 0 || this.value.length == 00) {
            $('.mid-error').remove();
        }
    });

    $('#admin_middle_name').blur(function() {
        if (!/^[a-zA-Z ]+$/.test(this.value) && this.value.length > 0 && $('.fn-error').length == 0){
            $(this).after('<span class="text-danger a-mid-error error">Please enter a valid name</span>');
        } else if(/^[a-zA-Z ]+$/.test(this.value) && $('.a-mid-error').length > 0 || this.value.length == 0){
            $('.a-mid-error').remove();
        }
    });

    $('#last_name').blur(function() {
        if (!/^[a-zA-Z ]+$/.test(this.value) && this.value.length > 0 && $('.l-error').length == 0){
            $(this).after('<span class="text-danger l-error error">Please enter a valid name</span>');
        } else if(/^[a-zA-Z ]+$/.test(this.value) && $('.l-error').length > 0 || this.value.length == 0){
            $('.l-error').remove();
        }
    });

    $('#admin_last_name').blur(function() {
        if (!/^[a-zA-Z ]+$/.test(this.value) && this.value.length > 0 && $('.fn-error').length == 0){
            $(this).after('<span class="text-danger a-l-error error">Please enter a valid name</span>');
        } else if(/^[a-zA-Z ]+$/.test(this.value) && $('.a-l-error').length > 0 || this.value.length == 0){
            $('.a-l-error').remove();
        }
    });
    

    // Add author button
    let stuff = `<div class="form-row">
                    <div class="col">
                        <input class="form-control" type="text" name="first_name" pattern="^[a-zA-Z ]+$" placeholder="First name">
                    </div>
                    <div class="col">
                        <input class="form-control" type="text" name="middle_name" pattern="^[a-zA-Z ]+$" placeholder="Middle name">
                    </div>
                    <div class="col">
                        <input class="form-control" type="text" name="last_name" pattern="^[a-zA-Z ]+$" placeholder="Last name">
                    </div>
                </div>`

    $('#add_author').click(function() {
        $(stuff).insertBefore('#add_author_button');
    });


    // City validation
    $('#city').blur(function(){
        if(!/^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$/.test(this.value) && this.value.length > 0 && $('.c-error').length == 0) {
            $(this).after('<span class="text-danger c-error error">Please enter a valid city</span>');
        } else if(/^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$/.test(this.value) && $('.c-error').length > 0) {
            $('.c-error').remove();
        }
    });

    // Clickable tags
    $('.tag').click(function(){
        if($('[name="tags"]').val().length == 0 && !$('[name="tags"]').val().includes(this.textContent)) {
            $('[name="tags"]').val(this.textContent);
        } else if($('[name="tags"]').val().length > 0 && !$('[name="tags"]').val().includes(this.textContent)){
            $('[name="tags"]').val($('[name="tags"]').val() + ', ' + this.textContent);
        }
    });

    // Submit button
    $('#submit').click(function(e) {
        if($('.error').length > 0) {
            alert("There are still errors. Please correct them before submitting.");
            e.preventDefault();
        }
    });

});