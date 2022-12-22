package com.example.demo.entity;


import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.Builder;
@Data
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Builder
@Table(name = "ORDER_DETAILS")
public class Order {
	@Id
	@GeneratedValue
	private int order_id;
	private String order_name;
	private int shippingCharge;
	private String status;
	private String order_day;
	
	

}
