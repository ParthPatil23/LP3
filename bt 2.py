// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {
    mapping(address => uint256) private balances;

    event Deposited(address indexed customer, uint256 amount);
    event Withdrawn(address indexed customer, uint256 amount);

    // Deposit ETH into the customer's bank account.
    function deposit() external payable {
        require(msg.value > 0, "Deposit must be greater than zero");

        balances[msg.sender] += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    // Withdraw an amount specified in wei.
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the balance before sending ETH.
        balances[msg.sender] -= amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Withdrawal failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Show the connected customer's balance in wei.
    function showBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}