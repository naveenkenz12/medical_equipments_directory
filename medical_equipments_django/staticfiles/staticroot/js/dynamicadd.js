$(document).ready(function(){
	var maxprefernces = 16;
	var counter = 1;
	var wrapper = $('.wrap');

    $(document).on('change',"#pref1",function(){
    	counter++;
    	if(counter<17)
    	{
    	var i = counter.toString();
    
        $(wrapper).append( ' <div class="form-group"><label class="control-label col-sm-4 col-md-4 col-xs-4" for="pref[]'+'"'+'>Preference '+i+'</label><div class="col-sm-4 col-md-4 col-xs-4"><input type="text" class="form-control" name="pref[]'+'"'+'placeholder="" id = "pref'+i+'"'+' > </div> </div>' );
    }
    });
    
});