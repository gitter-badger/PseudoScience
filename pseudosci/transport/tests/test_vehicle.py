#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ...units.general import Distance, Velocity, Acceleration, Mass
from ...movement import Movement, ComplexMovement
from ..vehicle import Vehicle
import pytest


class TestVehicle:
    """Tests unitaires de pseudosci.transport.Vehicle"""

    def test_init(self):
        """Tests du constructeur et des attributs simples de la classe."""
        v = Vehicle(velocity=Velocity(kph=50),
                    accel=Acceleration(kphs=20),
                    brake=Acceleration(kphs=30),
                    mass=Mass(kg=50))
        assert v.velocity.kph == 50
        assert v.accel.kphs == 20
        assert v.brake.kphs == 30
        assert v.mass.kg == 50
        v = Vehicle(velocity=Velocity(kph=50), accel=Acceleration(kphs=20))
        assert v.accel.mpss == v.brake.mpss
        v = Vehicle(velocity=Velocity(kph=50))
        assert v.accel.mpss == 0
        assert v.brake.mpss == 0

    def test_move(self):
        """Test de la méthode `move(distance)`"""
        cm = Vehicle(velocity=Velocity(kph=50),
                     accel=Acceleration(kphs=20),
                     brake=Acceleration(kphs=30)).move(Distance(km=5))
        m = Vehicle(velocity=Velocity(kph=50)).move(Distance(km=5))
        assert type(cm) is ComplexMovement
        assert m.distance.km == 5
        assert m.velocity.kph == 50
        assert cm.distance.km == 5
        assert cm.velocity.kph < 50

    def test_vehicle_force(self):
        """Test des attributs de la classe."""
        v = Vehicle(velocity=Velocity(mps=50),
                    accel=Acceleration(mpss=20),
                    brake=Acceleration(mpss=30),
                    mass=Mass(kg=50))
        assert v.accelforce.n == v.thrust.n == 1000
        assert v.brakeforce.n == 1500
