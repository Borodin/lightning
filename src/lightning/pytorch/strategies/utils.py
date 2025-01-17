# Copyright The Lightning AI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import importlib
from inspect import getmembers, isclass

from lightning.fabric.strategies import _StrategyRegistry
from lightning.fabric.utilities.registry import _is_register_method_overridden
from lightning.pytorch.strategies.strategy import Strategy


def _call_register_strategies(registry: _StrategyRegistry, base_module: str) -> None:
    # TODO(fabric): Remove this function once PL strategies inherit from Fabrics Strategy base class
    module = importlib.import_module(base_module)
    for _, mod in getmembers(module, isclass):
        if issubclass(mod, Strategy) and _is_register_method_overridden(mod, Strategy, "register_strategies"):
            mod.register_strategies(registry)
