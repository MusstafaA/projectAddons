

<?php

require_once ('delivery/src/Autoloader.php');
require_once ("delivery/lib/xmlrpc.inc");
require_once ("delivery/lib/xmlrpcs.inc");
$GLOBALS['xmlrpc_internalencoding']='UTF-8';

$user = 'admin';
$password = 'iti';
$dbname = 'iti9';

$server_url = 'http://localhost:8069'; 
$connexion = new xmlrpc_client($server_url . "/xmlrpc/common");
$connexion->setSSLVerifyPeer(0);

$c_msg = new xmlrpcmsg('login');
$c_msg->addParam(new xmlrpcval($dbname, "string"));
$c_msg->addParam(new xmlrpcval($user, "string"));
$c_msg->addParam(new xmlrpcval($password, "string"));
$c_response = $connexion->send($c_msg);


 if($_SERVER['REQUEST_METHOD'] === 'GET'){

	// // echo '<h2>XML-RPC AVEC OPENERP/ODOO ET PHP</h2>';
	
	// require_once ('delivery/src/Autoloader.php');

 //    // use PhpXmlRpc\Value;
 //    // use PhpXmlRpc\Request;
 //    // use PhpXmlRpc\Client;


	// require_once ("delivery/lib/xmlrpc.inc");
	// require_once ("delivery/lib/xmlrpcs.inc");
	// $GLOBALS['xmlrpc_internalencoding']='UTF-8';

	// $user = 'admin';
	// $password = 'iti';
	// $dbname = 'iti9';

	// $server_url = 'http://localhost:8069'; 
	// $connexion = new xmlrpc_client($server_url . "/xmlrpc/common");
	// $connexion->setSSLVerifyPeer(0);

	// $c_msg = new xmlrpcmsg('login');
	// $c_msg->addParam(new xmlrpcval($dbname, "string"));
	// $c_msg->addParam(new xmlrpcval($user, "string"));
	// $c_msg->addParam(new xmlrpcval($password, "string"));
	// $c_response = $connexion->send($c_msg);

	if ($c_response->errno != 0){
	    echo  '<p>error : ' . $c_response->faultString() . '</p>';
	}
	else{
	    
	    $uid = $c_response->value()->scalarval();

	    
	    // echo 'Partner created - partner_id = ' .  $uid .'<hr/>';



	    $domain_filter = array ( 
        new xmlrpcval(
            array(new xmlrpcval('state' , "string"), 
                  new xmlrpcval('=',"string"), 
                  new xmlrpcval('draft',"string")
                  ),"array"             
            ),
        ); 
    
	    $client = new xmlrpc_client($server_url . "/xmlrpc/object");
	    $client->setSSLVerifyPeer(0);

	    $msg = new xmlrpcmsg('execute'); 
	    $msg->addParam(new xmlrpcval($dbname, "string")); 
	    $msg->addParam(new xmlrpcval($uid, "int")); 
	    $msg->addParam(new xmlrpcval($password, "string")); 
	    $msg->addParam(new xmlrpcval("pos.order", "string")); 
	    $msg->addParam(new xmlrpcval("search", "string")); 
	    $msg->addParam(new xmlrpcval($domain_filter, "array")); 
	    $response = $client->send($msg);
	      
	    $result = $response->value();
	    $ids = $result->scalarval();


	   
	    $id_list = array();
	    
	    for($i = 0; $i < count($ids); $i++){
	        $id_list[]= new xmlrpcval($ids[$i]->me['int'], 'int');
	    }


///////////////// Main Orders list //////////////////////////

	    $field_list = array(
	    	new xmlrpcval("id", "int"),
	    	new xmlrpcval("name", "string"),
	    	new xmlrpcval("pos_reference", "string"),
	        new xmlrpcval("date_order", "string"),
	        new xmlrpcval("stage", "string"),
	        new xmlrpcval("state", "string"),
	        new xmlrpcval("amount_total", "string"),
	    ); 
	     
	    $msg = new xmlrpcmsg('execute');
	    $msg->addParam(new xmlrpcval($dbname, "string"));
	    $msg->addParam(new xmlrpcval($uid, "int"));
	    $msg->addParam(new xmlrpcval($password, "string"));
	    $msg->addParam(new xmlrpcval("pos.order", "string"));
	    $msg->addParam(new xmlrpcval("read", "string")); 
	    $msg->addParam(new xmlrpcval($id_list, "array")); 
	    $msg->addParam(new xmlrpcval($field_list, "array")); 

	    $resp = $client->send($msg);

	    if ($resp->faultCode()){
	        echo $resp->faultString();
	    }

	    $result = $resp->value()->scalarval();  
	    // print_r($result[4]);

////////////////////////////////////////////////////////////////////

//////////////// Order Line Details ////////////////////////////////



	    $order_id_list = array();     // array of orders ids 

	    for($i = 0; $i < count($result); $i++){
	        $order_id_list[]= new xmlrpcval($result[$i]->me['struct']['id']->me['int'], 'int');
	    }



	    $order_line_domain_filter = array (               // condition to select all order lines ids related to kitchen orders
        new xmlrpcval(
            array(new xmlrpcval('order_id' , "string"), 
                  new xmlrpcval('in',"string"), 
                  new xmlrpcval($order_id_list,"array")
                  ),"array"             
            ),
        ); 
    
	    // $client = new xmlrpc_client($server_url . "/xmlrpc/object");
	    // $client->setSSLVerifyPeer(0);

	    $order_line_msg = new xmlrpcmsg('execute'); 
	    $order_line_msg->addParam(new xmlrpcval($dbname, "string")); 
	    $order_line_msg->addParam(new xmlrpcval($uid, "int")); 
	    $order_line_msg->addParam(new xmlrpcval($password, "string")); 
	    $order_line_msg->addParam(new xmlrpcval("pos.order.line", "string")); 
	    $order_line_msg->addParam(new xmlrpcval("search", "string")); 
	    $order_line_msg->addParam(new xmlrpcval($order_line_domain_filter, "array")); 
	    $order_line_response = $client->send($order_line_msg);
	      
	    $order_line_result = $order_line_response->value();
	    $order_line_ids = $order_line_result->scalarval();	   

	    //print_r($order_line_ids);



 ////////////////////// getting certain fields of order lines /////////////////////////////

	    $order_line_id_list = array();
	    
	    for($i = 0; $i < count($order_line_ids); $i++){
	        $order_line_id_list[]= new xmlrpcval($order_line_ids[$i]->me['int'], 'int');
	    }




	    $order_line_field_list = array(
	    	new xmlrpcval("product_id", "string"),
	    	new xmlrpcval("qty", "string"),
	    	new xmlrpcval("order_id", "string"),
	    	//new xmlrpcval("price_subtotal_incl", "string"),
	    ); 
	     
	    $order_line_details_msg = new xmlrpcmsg('execute');
	    $order_line_details_msg->addParam(new xmlrpcval($dbname, "string"));
	    $order_line_details_msg->addParam(new xmlrpcval($uid, "int"));
	    $order_line_details_msg->addParam(new xmlrpcval($password, "string"));
	    $order_line_details_msg->addParam(new xmlrpcval("pos.order.line", "string"));
	    $order_line_details_msg->addParam(new xmlrpcval("read", "string")); 
	    $order_line_details_msg->addParam(new xmlrpcval($order_line_id_list, "array")); 
	    $order_line_details_msg->addParam(new xmlrpcval($order_line_field_list, "array")); 

	    $order_line_resp = $client->send($order_line_details_msg);

	    if ($order_line_resp->faultCode()){
	        echo $order_line_resp->faultString();
	    }

	    $order_line_details_result = $order_line_resp->value()->scalarval();  

	    //print_r($order_line_details_result[10]);
	    
	    $full_order_data = array();
	    $full_order_data['order_line'] = $order_line_details_result;
	    $full_order_data['order'] = $result;

	    //print_r($full_order_data);




////////////////////////////////////////////////////////////////////////



	    
	    header('Content-Type: application/json');
  		//echo json_encode($result);
	    echo json_encode($full_order_data);


	    //print_r($result);
	    // var_dump($result[0]);
	    // echo '<hr />';
	    // echo '<h2>Orders:</h2>';
	   
	    // for($i = 0; $i < count($result); $i++){

	    //     echo '<h1>' . $result[$i]->me['struct']['name']->me['string'] . '</h1>'
	    //        . '<ol>'
	    //        . '<li><strong>price</strong> : ' . $result[$i]->me['struct']['pos_reference']->me['string'] . '</li>'
	    //        . '<li><strong>Current stage</strong> : ' . $result[$i]->me['struct']['stage']->me['string'] . '</li>'
	    //        . '<li><strong>State</strong> : ' . $result[$i]->me['struct']['state']->me['string'] . '</li>'
	    //        . '<li><strong>Order date</strong> : ' . $result[$i]->me['struct']['date_order']->me['string'] . '</li>'
	    //        . '<li><strong>Order ID</strong> : ' . $result[$i]->me['struct']['id']->me['int'] . '</li>'
	    //        . '</ol>'     
	    //        . '<hr />';
	    // }




	}




}
else if($_SERVER['REQUEST_METHOD'] === 'POST'){

	  header("Access-Control-Allow-Origin: " . $_SERVER['HTTP_ORIGIN']);
	  header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
	  header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");

	  $postdata = file_get_contents("php://input");
      $request = json_decode($postdata);
      $order_id =  $request->order_id;  
      $current_stage =  $request->Cstage ;

	if ($c_response->errno != 0){
	    echo  '<p>error : ' . $c_response->faultString() . '</p>';
	}
	else{
	    
	    $uid = $c_response->value()->scalarval();


	    $id_list = array();
	    $id_list[]= new xmlrpcval($order_id , 'int');

	    $values = array ( 
	        'stage'=>new xmlrpcval($current_stage , "string"),            
	        ); 
	    
	    $client = new xmlrpc_client($server_url . "/xmlrpc/object");
	    $client->setSSLVerifyPeer(0);

	    $msg = new xmlrpcmsg('execute'); 
	    $msg->addParam(new xmlrpcval($dbname, "string")); 
	    $msg->addParam(new xmlrpcval($uid, "int")); 
	    $msg->addParam(new xmlrpcval($password, "string")); 
	    $msg->addParam(new xmlrpcval("pos.order", "string")); 
	    $msg->addParam(new xmlrpcval("write", "string")); 
	    $msg->addParam(new xmlrpcval($id_list, "array"));
	    $msg->addParam(new xmlrpcval($values, "struct")); 
	    $response = $client->send($msg);

	    if ($response->faultCode()){
	        echo $response->faultString();
	    }    
	    
	    




	}




}


?>

