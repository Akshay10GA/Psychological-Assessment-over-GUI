00package com.example.demo.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.entity.Customer;


public interface CustomerRepository extends JpaRepository<Customer, Integer> {

}
