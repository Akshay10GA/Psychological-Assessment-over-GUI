package com.example.demo.serviceImpl;

import java.util.List;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;

import com.example.demo.Repository.OrderRepository;
import com.example.demo.Service.OrderService;
import com.example.demo.dto.OrderDTO;
import com.example.demo.entity.Order;

@Service
public class orderServiceimpl implements OrderService {
	@Autowired
	OrderRepository or;

	@Override
	public Order createOrder(OrderDTO ort) {
		Order o = Order.builder()
				.order_name(ort.getOrder_name()).shippingCharge(ort.getShippingCharge())
				.status(ort.getStatus()).order_day(ort.getOrder_day()).build();
		return or.save(o);
	}

	@Override
	public Order getorder(int id) {
		return or.findById(id).get();
	}

	@Override
	public List<Order> getAllOrders() {
		return or.findAll();
	}

	@Override
	public String deleteOrder(int id) {
		or.deleteById(id);
		return "Order deleted successfully.";
	}

	@Override
	public String updateOrder(int id, OrderDTO ort) {
		Order o = or.findById(id).get();
		
		Order o1 = Order.builder()
				.order_name(ort.getOrder_name()).shippingCharge(ort.getShippingCharge())
				.status(ort.getStatus()).order_day(ort.getOrder_day()).build();
		
		or.save(o1);
		
		return "Order updated successfully.";
	}

	@Override
	public String deleteAllOrders() {
		or.deleteAll();
		return "All orders deleted successfully.";
	}

	
}
