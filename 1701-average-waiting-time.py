# There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

# arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
# timei is the time needed to prepare the order of the ith customer.
# When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

# Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.


def averageWaitingTime(customers: list[list[int]]) -> float:
    total_customers = len(customers)
    total_time = 0
    waiting_time = 0
    while customers:
        arival_time, time = customers.pop(0)
        if arival_time <= total_time:
            waiting_time += (total_time + time) - arival_time
            total_time += time
        else:
            waiting_time += (arival_time + time) - arival_time
            total_time = arival_time + time
    return waiting_time/total_customers

if __name__ == "__main__":
    customers = [[5,2],[5,4],[10,3],[20,1]]
    print(f'The average waiting time is : {averageWaitingTime(customers=customers)}')