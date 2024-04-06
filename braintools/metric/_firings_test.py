# Copyright 2024- BrainPy Ecosystem Limited. All Rights Reserved.
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
# ==============================================================================

# -*- coding: utf-8 -*-


import unittest
import braincore as bc
import jax.numpy as jnp
import braintools as bt


class TestFiringRate(unittest.TestCase):
  def test_fr1(self):
    spikes = jnp.ones((1000, 10))
    print(bt.metric.firing_rate(spikes, 1.))

  def test_fr2(self):
    bc.random.seed()
    spikes = bc.random.random((1000, 10)) < 0.2
    print(bt.metric.firing_rate(spikes, 1.))
    print(bt.metric.firing_rate(spikes, 10.))

  def test_fr3(self):
    bc.random.seed()
    spikes = bc.random.random((1000, 10)) < 0.02
    print(bt.metric.firing_rate(spikes, 1.))
    print(bt.metric.firing_rate(spikes, 5.))
