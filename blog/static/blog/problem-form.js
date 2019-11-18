$("#seeAnotherField").change(function() {
			if ($(this).val() == "abandon_vehicle") {
				$('#abandon_vehicle').show();
				$('#abandon_vehicle').attr('required','');
				$('#abandon_vehicle').attr('data-error', 'This field is required.');
			} else if($(this).val() == "city_recreation" || $(this).val() == "code_enforcement" ||$(this).val() == "general_park_maintenance" ||$(this).val() == "graffiti_removal" ||$(this).val() == "hiking_trails" ||$(this).val() == "landscape_zones" ||$(this).val() == "parking" ||$(this).val() == "request_an_inspection" ||$(this).val() == "street_light_outage" ||$(this).val() == "street_sidewalk_right_of_way_maintenance" ||$(this).val() == "street_sweeping" ||$(this).val() == "traffic_signal" ||$(this).val() == "trash_recycling" ||$(this).val() == "trees" ||$(this).val() == "Others") {
				$('#abandon_vehicle').hide();
				$('#abandon_vehicle').removeAttr('required');
				$('#abandon_vehicle').removeAttr('data-error');
			}
		});
		$("#seeAnotherField").trigger("change");



$("#seeAnotherFieldGroup").change(function() {
			if ($(this).val() == "no") {
				$('#otherFieldGroupDiv').show();
				$('#otherField1').attr('required','');
				$('#otherField1').attr('data-error', 'This field is required.');
        $('#otherField2').attr('required','');
				$('#otherField2').attr('data-error', 'This field is required.');
			} else {
				$('#otherFieldGroupDiv').hide();
				$('#otherField1').removeAttr('required');
				$('#otherField1').removeAttr('data-error');
        $('#otherField2').removeAttr('required');
				$('#otherField2').removeAttr('data-error');
			}
		});
		$("#seeAnotherFieldGroup").trigger("change");


var $select = $('#seeAnotherField');
$('a[href="#problem-form"]').click(function () {
    $select.val( $(this).data('select') );
});