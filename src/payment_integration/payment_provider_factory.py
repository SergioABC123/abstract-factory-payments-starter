from abc import ABC, abstractmethod

from .authorizer import Authorizer
from .refund_processor import RefundProcessor
from .webhook_verifier import WebhookVerifier


class PaymentProviderFactory(ABC):
    """Crea las tres capacidades de una misma familia de pagos."""

    @abstractmethod
    def create_authorizer(self) -> Authorizer:
        pass

    @abstractmethod
    def create_refund_processor(self) -> RefundProcessor:
        pass

    @abstractmethod
    def create_webhook_verifier(self) -> WebhookVerifier:
        pass
