import click
from utils import add_policy_to_all_users

ALL_PLAX_DEV_USERS = [
    "abbygeorge@uchicago.edu",
    "aprokh@uchicago.edu",
    "atharvar@uchicago.edu",
    "avantol@uchicago.edu",
    "diw@uchicago.edu",
    "emalinowski@uchicago.edu",
    "fantix@uchicago.edu",
    "fauzi@uchicago.edu",
    "giangbui@uchicago.edu",
    "mlukowski@uchicago.edu",
    "mshao1@uchicago.edu",
    "qshu@uchicago.edu",
    "reubenonrye@uchicago.edu",
    "ribeyre@uchicago.edu",
    "rudyardrichter@uchicago.edu",
    "thanhnd@uchicago.edu",
    "vzpgb@uchicago.edu",
    "yajingt@uchicago.edu"
]

ALL_DEV_USERS = ALL_PLAX_DEV_USERS + [
    "dgrantkeane@uchicago.edu",
    "dmiller15@uchicago.edu",
    "fitz@uchicago.edu",
    "mikeabreu@uchicago.edu",
    "kuangx@uchicago.edu",
    "zgowani@uchicago.edu",
    "zlchitty@uchicago.edu"]

ALL_BIO_USERS = [
    "cgmeyer@uchicago.edu",
    "fan1@uchicago.edu",
    "yilinxu@uchicago.edu",
]

ALL_COMMONS = ["accountprod",
               "anvil",
               "anvilstaging",
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

def add_policy_for_users(root, users, commons, policy):
    """
    Add policy
    :param root: path to common users. Ex. /Users/giangbui/Projects/commons-users/user\
    :param users: list of users\
    :param commons: list of commons\
    :param policy: policy
    :return:
    """

    for common in commons:
        add_policy_to_all_users(policy, users, root + "/" + common + "/user.yaml")


def remove_user_from_all_commons(user):
    raise NotImplementedError


def add_user_to_common(user, user_yaml, json_block):
    raise NotImplementedError


@click.group()
def cli1():
    pass


@cli1.command()
@click.option('--root', required=True, help='path to common users dir')
@click.option('--policy', required=True, help='policy')
def add_policy(root, policy):
    """add policy."""
    add_policy_for_users(root, ALL_DEV_USERS, ALL_COMMONS, policy)


cli = click.CommandCollection(sources=[cli1])
if __name__ == "__main__":
    cli()
