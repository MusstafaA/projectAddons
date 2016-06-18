

<?php

require_once ('delivery/src/Autoloader.php');
require_once ("delivery/lib/xmlrpc.inc");
require_once ("delivery/lib/xmlrpcs.inc");
$GLOBALS['xmlrpc_internalencoding']='UTF-8';

$user = 'admin';
$password = 'iti';
$dbname = '';

$server_url = 'http://localhost:8069'; 
$connexion = new xmlrpc_client($server_url . "/xmlrpc/common");
$connexion->setSSLVerifyPeer(0);

$c_msg = new xmlrpcmsg('login');
$c_msg->addParam(new xmlrpcval($dbname, "string"));
$c_msg->addParam(new xmlrpcval($user, "string"));
$c_msg->addParam(new xmlrpcval($password, "string"));
$c_response = $connexion->send($c_msg);


 if($_SERVER['REQUEST_METHOD'] === 'GET'){

	if ($c_response->errno != 0){
	    echo  '<p>error : ' . $c_response->faultString() . '</p>';
	}
	else{
	    
	    $uid = $c_response->value()->scalarval();


         $order_states = array();
	        $order_states[]= new xmlrpcval('draft', 'string');
	        $order_states[]= new xmlrpcval('out', 'string');


	    $domain_filter = array (            
        new xmlrpcval(
            array(new xmlrpcval('state' , "string"), 
                  new xmlrpcval('in',"string"), 
                  new xmlrpcval($order_states,"array")
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
	        new xmlrpcval("partner_id", "string"),
	        new xmlrpcval("state", "string"),
	        new xmlrpcval("amount_total", "string"),
	        new xmlrpcval("manuf_time", "string"),
	        new xmlrpcval("delivery_time", "string"),

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
	   
	    $full_order_data = array();
	    //$full_order_data['order_line'] = $order_line_details_result;
	    $full_order_data['order'] = $result;

////////////////////////////////////////////////////////////////////////

	    
	    header('Content-Type: application/json');
  		//echo json_encode($result);
	    echo json_encode($full_order_data);
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

