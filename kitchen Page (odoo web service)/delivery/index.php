<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>

    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/my-bootstrap.css">

    <!-- jQuery library -->
    <script src="js/jquery-1.11.2.js"></script>

    <!-- Latest compiled JavaScript -->
    <script src="js/bootstrap.js"></script>


    <link href="css/css/style.css" rel="stylesheet"/>
</head>
<body ng-app="MyApp">
<div class="container" ng-controller="Orders as control">

          <div class="panel panel-default">
                <!-- Default panel contents -->
              <div class="panel-heading"><span class="lead">List of Orders </span></div>
              <div class="tablecontainer">
<!--                   <table class="table table-hover">
                      <thead>
                          <tr>
                              <th>ID</th>
                              <th>Name</th>
                              <th>Order Date</th>
                              <th>Current Stage</th>
                              <th>State</th>
                              <th width="100">
                          </tr>
                      </thead>
                      <tbody>
                          <tr ng-repeat="order in control.orders">
                              <td><span ng-bind="order.me['struct']['id'].me['int']"></span></td>
                              <td><span ng-bind="order.me['struct']['name'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['date_order'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['stage'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['state'].me['string']"></span></td>
                              <td>
                              <button type="button" ng-click="control.editStage(order.me['struct']['id'].me['int'],order.me['struct']['stage'].me['string'])" ng-class="{'btn btn-danger custom-width': order.me['struct']['stage'].me['string'] == 'kitchen' , 'btn btn-warning custom-width': order.me['struct']['stage'].me['string'] == 'Ready for delivery', 'btn btn-primary custom-width': order.me['struct']['stage'].me['string'] == 'Delivery', 'btn btn-success custom-width': order.me['struct']['stage'].me['string'] == 'Delivered'}">{{order.me['struct']['stage'].me['string']}}</button>
                          	  </td>
                          </tr>
                      </tbody>
                  </table> -->


                  <table class="table table-hover">
                    <thead>
                      <tr>
                          <th>ID</th>
                          <th>Name</th>
                          <th>Order Date</th>
                          <th>Current Stage</th>
                          <th>State</th>
                          <th>Total price</th>
                          <th width="100">
                      </tr>
                    </thead>

                    <tbody ng-repeat="order in control.orders" >
                        
                          <tr  data-toggle="collapse" data-target="#{{order.me['struct']['id'].me['int']}}" class="clickable">
                              <td><span ng-bind="order.me['struct']['id'].me['int']"></span></td>
                              <td><span ng-bind="order.me['struct']['name'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['date_order'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['stage'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['state'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['amount_total'].me['double']"></span></td>
                              <td>
                              <button type="button" ng-click="control.editStage(order.me['struct']['id'].me['int'],order.me['struct']['stage'].me['string'])" ng-class="{'btn btn-danger custom-width': order.me['struct']['stage'].me['string'] == 'kitchen' , 'btn btn-warning custom-width': order.me['struct']['stage'].me['string'] == 'Ready for delivery', 'btn btn-primary custom-width': order.me['struct']['stage'].me['string'] == 'Delivery', 'btn btn-success custom-width': order.me['struct']['stage'].me['string'] == 'Delivered'}">{{order.me['struct']['stage'].me['string']}}</button>
                              </td>
                          </tr>

                          <tr>
                              <td colspan="3">
                                  <div id="{{order.me['struct']['id'].me['int']}}" class="collapse">
                                          <table class="table ">
                                            <thead>
                                              <tr>
                                                <th>Product</th>
                                                <!-- <th>unit Price</th> -->
                                                <th>Amount</th>
                                              </tr>
                                            </thead>

                                            <tr ng-repeat="orderLine in control.order_details" ng-if="orderLine.me['struct']['order_id'].me['array'][0].me['int'] == order.me['struct']['id'].me['int']">
                                                <td><span ng-bind="orderLine.me['struct']['product_id'].me['array'][1].me['string']"></span></td>
                                                <!-- <td><span ng-bind="orderLine.me['struct']['order_id'].me[0]['int']"></span></td> -->
                                                <td><span ng-bind="orderLine.me['struct']['qty'].me['double']"></span></td>
                                            </tr>    

                                          </table>

                                  </div>
                              </td>
                          </tr>
                      
                    </tbody>
                    </table>





              </div>
          </div>
      </div>








   
</div>
<script src="js/js/angular.js"></script>
<script src="js/js/app.js"></script>
<script src="js/js/services.js"></script>
<script src="js/js/controllers.js"></script>
</body>
</html>



