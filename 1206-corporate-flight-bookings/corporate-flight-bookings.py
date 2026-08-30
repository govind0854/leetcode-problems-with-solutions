class Solution(object):
    def corpFlightBookings(self, bookings, n):
        flights = [0] * (n + 1)

        for l, r, val in bookings:
            flights[l - 1] += val
            flights[r] -= val

        for i in range(1, n):
            flights[i] += flights[i - 1]

        return flights[:n]