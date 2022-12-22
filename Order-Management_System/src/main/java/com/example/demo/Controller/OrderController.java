package com.example.demo.Controller;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.Service.OrderService;
import com.example.demo.dto.OrderDTO;
import com.example.demo.entity.Order;


@RestController
public class OrderController {

	@Autowired(required = true)
	OrderService or;
	
	@PostMapping("/order")
	public  ResponseEntity<Order> createStudent(@RequestBody @Valid OrderDTO ort )
	{	 
		Order o=or.createOrder(ort);
		if(o!=null)
			return new ResponseEntity<Order>(o, HttpStatus.CREATED);
		
	   return new ResponseEntity<Order>(o, HttpStatus.BAD_REQUEST);
	}
	
	@GetMapping("/order/{id}")
	public ResponseEntity<Order> getStudent(@PathVariable int id)
	{
		try {
		Order o=or.getorder(id);
		if(o!=null)
			return new ResponseEntity<Order>(o, HttpStatus.OK);
		}catch(Exception e)
		{		
//	       throw new UserNotFoundException("user not found");
			e.printStackTrace();		}
		 return new ResponseEntity<Order>(HttpStatus.NOT_FOUND);
	}
//	
//	
	@GetMapping("/orders")
	public ResponseEntity<List<Order>> getOrder()
	{
		try {
			List<Order> slist=or.getAllOrders();
			if(slist!=null)
				return new ResponseEntity<List<Order>>(slist, HttpStatus.OK);
			}catch(Exception e)
			{		
		       e.printStackTrace();
			}
			 return new ResponseEntity<List<Order>>(HttpStatus.NOT_FOUND);
		
		
	}
	
	@PutMapping("/order/{id}")
	public String updateOrder(@PathVariable("id") int id,@RequestBody @Valid OrderDTO ort)
	{
		return or.updateOrder(id, ort);
	}
	
	
	
	@DeleteMapping("/order/{id}")
	public String deleteOrder(@PathVariable("id") int id)
	{
		return or.deleteOrder(id);
		
	}

	@DeleteMapping("/orders")
	public String deleteOrders()
	{
		return or.deleteAllOrders();		
	}
}
