angular.module('MyApp')
    .controller('Orders', ['UserService','$timeout', function (UserService , $timeout) {
            var self = this;


            UserService.list().success(function(data){
                self.orders = data;
            });



              // Function to replicate setInterval using $timeout service.
              self.intervalFunction = function(){
                $timeout(function() {
                  UserService.list();
                  self.intervalFunction();
                }, 1000)
              };

              //Kick off the interval
              self.intervalFunction();


            self.editStage = function(id,current_stage){
                  console.log('id to be edited', id);
            		  console.log('stage to be edited', current_stage);
            		  UserService.editStage(id , current_stage);

              };
               



        }])


