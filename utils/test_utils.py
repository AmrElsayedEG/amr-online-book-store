from mixer.backend.django import Mixer, GenFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.test import TestCase

mixer = Mixer(factory=GenFactory)