$(document).ready(function() {
    $('#bchangeform').bootstrapValidator({
        
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:{
             name:{
                validators:{
                    notEmpty:{
                        message: 'Name can not be empty'
                    }
                }
            },
            rollno:{
                validators:{
                    notEmpty:{
                        message: 'Roll No field is empty'
                    },
                    stringLength:{
                        min:9,
                        max:9,
                        message: 'Roll Number must be of 9 Digits'
                    },
                    regexp:{
                        regexp: /^15/,
                        message: 'Roll Number must be of the form 15XXXXXXX only'

                    }
             }
            },
            cpi:{
                validators:{
                    notEmpty:{
                        message: 'CPI can\'t be empty'
                    },
                    between:{
                        min: 0,
                        max: 10,
                        message: 'CPI must be in [0,10]'
                    }
                }
            },
            pref1:{
                validators:{
                    notEmpty:{
                        message:'Prefernce can not be empty'
                    }

                }
            },
            pref2:{
                validators:{
                    notEmpty:{
                        message:'Prefernce can not be empty'
                    }

                }
            },
            pbranch:{
                validators:{
                    notEmpty:{
                        message:'Present Branch can not be empty'
                    }

                }

            }

        }


    });
     

});