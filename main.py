from utils import add_policy_to_all_users


def add_policy_for_all_dev_in_all_commons(policy):

    root = "/Users/giangbui/Projects/commons-users/users"
    users = ["abbygeorge@uchicago.edu",
             "aprokh@uchicago.edu",
             "atharvar@uchicago.edu",
             "avantol@uchicago.edu",
             "cdis.autotest@gmail.com",
             "cgmeyer@uchicago.edu",
             "dgrantkeane@uchicago.edu",
             "diw@uchicago.edu",
             "dmiller15@uchicago.edu",
             "emalinowski@uchicago.edu",
             "fan1@uchicago.edu",
             "fantix@uchicago.edu",
             "fauzi@uchicago.edu",
             "fitz@uchicago.edu",
             "giangbui@uchicago.edu",
             "mlukowski@uchicago.edu",
             "mshao1@uchicago.edu",
             "mikeabreu@uchicago.edu",
             "qshu@uchicago.edu",
             "reubenonrye@uchicago.edu",
             "ribeyre@uchicago.edu",
             "rudyardrichter@uchicago.edu",
             "thanhnd@uchicago.edu",
             "vzpgb@uchicago.edu",
             "kuangx@uchicago.edu",
             "yajingt@uchicago.edu",
             "yilinxu@uchicago.edu",
             "zgowani@uchicago.edu",
             "zlchitty@uchicago.edu"]
    commons = ["accountprod",
               "anvil",
               "bpa",
               "canine",
               "cvb",
               "dcfqa",
               "dcp",
               "dev",
               "edc",
               "genomel",
               "kfqa",
               "ncicrdcdemo",
               "ndh",
               "qa",
               "stagingdatastage",
               "vadcprod"]

    for common in commons:
        add_policy_to_all_users(policy, users, root + "/" + common + "/user.yaml")


def main():
    add_policy_for_all_dev_in_all_commons("prometheus")


if __name__ == "__main__":
    main()
