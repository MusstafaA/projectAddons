angular.module('MyApp')
.factory('UserService', ['$http', function($http){
        return {
            'list': function(){
                return $http.get('http://localhost/orders.php')
            },

            'editStage': function(id , currentStage){

                            if(currentStage == 'kitchen')
                                {
                                      current_stage = 'Ready for delivery';
                                }
                            else if(currentStage == 'Ready for delivery')
                                {
                                      current_stage = 'Delivery';
                                }    
                            else if(currentStage == 'Delivery')
                                {
                                      current_stage = 'Delivered';
                                }
                            else
                                {
                                      current_stage = 'kitchen';
                                }

                                var request=$http({
                                method: "post",
                                url:"http://localhost/orders.php",
                                data:{
                                        order_id: id,
                                        Cstage : current_stage
                                    },
                                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
                            });
            }
        };
    }]);
