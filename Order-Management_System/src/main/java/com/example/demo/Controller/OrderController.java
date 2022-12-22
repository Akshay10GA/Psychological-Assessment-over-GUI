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
	
	@PostMapping("/student")
	public  ResponseEntity<Order> createStudent(@RequestBody @Valid OrderDTO ort )
	{	 
//		, @DateTimeFormat(iso = DateTimeFormat.ISO.DATE_TIME)Order order
		Order o=or.createOrder(ort);
		if(o!=null)
			return new ResponseEntity<Order>(o, HttpStatus.CREATED);
		
	   return new ResponseEntity<Order>(o, HttpStatus.BAD_REQUEST);
	}
	
//	@GetMapping("/student/{id}")
//	public ResponseEntity<Student> getStudent(@PathVariable int id)
//	{
//		try {
//		Student s=ss.getStudent(id);
//		if(s!=null)
//			return new ResponseEntity<Student>(s, HttpStatus.OK);
//		}catch(Exception e)
//		{		
//	       throw new UserNotFoundException("user not found");
//		}
//		 return new ResponseEntity<Student>(HttpStatus.NOT_FOUND);
//	}
//	
//	
//	@GetMapping("/students")
//	public ResponseEntity<List<Student>> getStudents()
//	{
//		try {
//			List<Student> slist=ss.getAllStudents();
//			if(slist!=null)
//				return new ResponseEntity<List<Student>>(slist, HttpStatus.OK);
//			}catch(Exception e)
//			{		
//		       e.printStackTrace();
//			}
//			 return new ResponseEntity<List<Student>>(HttpStatus.NOT_FOUND);
//		
//		
//	}
//	
//	@PutMapping("/student/{id}")
//	public String updateStudent(@PathVariable("id") int id,@RequestBody @Valid StudentDTO st)
//	{
//		return ss.updateStudent(id,st);
//	}
//	
//	@PutMapping("/student/{id}/{name}")
//	public Student updateStudentName(@PathVariable("id") int id,@PathVariable("name") String name)
//	{
//		return ss.updateStudentName(id,name);
//	}
//	
//	
//	@DeleteMapping("/student/{id}")
//	public String deleteStudent(@PathVariable("id") int id)
//	{
//		return ss.deleteStudent(id);
//		
//	}
//
//	@DeleteMapping("/students")
//	public String deleteStudents()
//	{
//		return ss.deleteAllStudents();
//		
//	}
}
