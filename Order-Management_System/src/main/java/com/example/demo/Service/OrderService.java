package com.example.demo.Service;

import java.util.List;

import org.springframework.stereotype.Component;

import com.example.demo.dto.OrderDTO;
import com.example.demo.entity.Order;

@Component
public interface OrderService {
	public Order createOrder(OrderDTO ort);
	public Order getorder(int id);
	public List<Order> getAllOrders();
	public String deleteOrder(int id);
	public String updateOrder(int id,OrderDTO ort);
	public String deleteAllOrders();
	
}
