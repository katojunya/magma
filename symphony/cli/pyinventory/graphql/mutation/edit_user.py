#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from gql.gql.client import OperationException
from gql.gql.reporter import FailedOperationException
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional
from time import perf_counter
from dataclasses_json import DataClassJsonMixin

from ..fragment.user import UserFragment, QUERY as UserFragmentQuery
from ..input.edit_user import EditUserInput


QUERY: List[str] = UserFragmentQuery + ["""
mutation EditUserMutation($input: EditUserInput!) {
  editUser(input: $input) {
    ...UserFragment
  }
}

"""]

@dataclass
class EditUserMutation(DataClassJsonMixin):
    @dataclass
    class EditUserMutationData(DataClassJsonMixin):
        @dataclass
        class User(UserFragment):
            pass

        editUser: User

    data: EditUserMutationData

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, input: EditUserInput) -> EditUserMutationData.User:
        # fmt: off
        variables = {"input": input}
        try:
            start_time = perf_counter()
            response_text = client.call(''.join(set(QUERY)), variables=variables)
            res = cls.from_json(response_text).data
            elapsed_time = perf_counter() - start_time
            client.reporter.log_successful_operation("EditUserMutation", variables, elapsed_time)
            return res.editUser
        except OperationException as e:
            raise FailedOperationException(
                client.reporter,
                e.err_msg,
                e.err_id,
                "EditUserMutation",
                variables,
            )
