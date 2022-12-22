package com.example.demo.Repository;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.example.demo.entity.Order;

//@RepositoryRestResource(collectionResourceRel="Oreder",path = "Order")

public interface OrderRepository extends JpaRepository<Order, Integer> {

}
