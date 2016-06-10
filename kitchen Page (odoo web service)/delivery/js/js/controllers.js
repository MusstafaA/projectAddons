angular.module('MyApp')
    .controller('Orders', ['UserService','$interval', function (UserService , $interval) {
            var self = this;


            // UserService.list().success(function(data){
            //     self.orders = data;
            // });



            $interval(function(){
                  UserService.list().success(function(data){
                  self.orders = data['order'];
                  self.order_details = data['order_line'];                

              });

            },8000);
           



            self.editStage = function(id,current_stage){
                  console.log('id to be edited', id);
            		  console.log('stage to be edited', current_stage);
            		  UserService.editStage(id , current_stage);


                  if(current_stage == 'kitchen')
                      {
                            self.bclass = 'btn-primary'
                      }
                  else if(current_stage == 'Ready for delivery')
                      {
                            self.bclass = 'btn-warning'
                      }    
                  else if(current_stage == 'Delivery')
                      {
                            self.bclass = 'btn-success';
                      }
                  else
                      {
                            self.bclass = 'btn-danger';
                      }


              };
               



        }])


