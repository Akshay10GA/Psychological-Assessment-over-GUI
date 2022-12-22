package com.example.demo.dto;



import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import javax.validation.constraints.Size;



import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
@Builder
public class OrderDTO {
	@NotBlank(message = "Order_Name can't be empty")
	@NotNull(message = "Order_Name can't be  null")
	@Size(min = 3, max = 20, message = "Order_Name must be within 3-20 characters")
	String order_name;
	
//	@NotBlank(message = "Shipping charges can't be empty")
//	@NotNull(message = "Shipping charges can't be  null")
	int shippingCharge;
	
	@NotBlank(message = "Status can't be empty")
	@NotNull(message = "Status charges can't be  null")
	String status;
	
	@NotBlank(message = "Order Day can't be empty")
	@NotNull(message = "Order Day can't be null")
	String order_day;

}