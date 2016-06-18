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
                  <table class="table table-hover">
                    <thead>
                      <tr>
                          <th>ID</th>
                          <th>Name</th>
                          <th>Order Date</th>
                          <th>State</th>
                          <th>Total price</th>
                          <th>Manufacturing Time</th>
                          <th>Delivery Time</th>
                      </tr>
                    </thead>

                    <tbody ng-repeat="order in control.orders" >
                        
                          <tr>
                              <td><span ng-bind="order.me['struct']['id'].me['int']"></span></td>
                              <td><span ng-bind="order.me['struct']['name'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['date_order'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['state'].me['string']"></span></td>
                              <td><span ng-bind="order.me['struct']['amount_total'].me['double']"></span></td>
                              <td>
                               <span ng-click="control.editStage(order.me['struct']['id'].me['int'],order.me['struct']['state'].me['string'])" ng-class="{'btn btn-danger custom-width': order.me['struct']['manuf_time'].me['string'] >= '0:25:01','btn btn-success custom-width': order.me['struct']['manuf_time'].me['string'] < '0:25:01'}" ng-bind="order.me['struct']['manuf_time'].me['string']"></span>
                              </td>
                              <td>
                                <span ng-click="control.editStage(order.me['struct']['id'].me['int'],order.me['struct']['state'].me['string'])" ng-class="{'btn btn-danger custom-width': order.me['struct']['delivery_time'].me['string'] >= '0:25:01','btn btn-success custom-width': order.me['struct']['manuf_time'].me['string'] < '0:25:01'}" ng-bind="order.me['struct']['delivery_time'].me['string']"></span>
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