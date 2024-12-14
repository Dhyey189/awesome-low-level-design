from split_wise import SplitWise

class SplitWiseDemo:
    @staticmethod
    def run():
        split_wise = SplitWise.get_instance()

        u1 = split_wise.add_user("Dhyey", "d@d.com")
        u2 = split_wise.add_user("Karan", "k@k.com")
        u3 = split_wise.add_user("Mavan", "m@m.com")
        u4 = split_wise.add_user("Aayush", "a@a.com")

        g1 = split_wise.add_group(u1, "Group1", "Trip to manali", [u1, u2, u3])
        # g2 = split_wise.add_group(u2, "Group2", "Trip to lonavala", [u2, u3, u4])

        expense1 = split_wise.add_expense(
            u1,
            g1,
            "paragliding",
            3000,
            [u1, u2, u3],
            u2
        )

        u2.update_balances(u1, 500)

        print(u1._id, u1.get_balances())
        print(u2._id, u2.get_balances())
        print(u3._id, u3.get_balances())



if __name__ == "__main__":
    SplitWiseDemo.run()