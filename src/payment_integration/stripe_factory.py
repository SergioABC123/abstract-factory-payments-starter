from .authorizer import Authorizer
from .refund_processor import RefundProcessor
from .webhook_verifier import WebhookVerifier
from .payment_provider_factory import PaymentProviderFactory
from .stripe_authorizer import StripeAuthorizer
from .stripe_refund_processor import StripeRefundProcessor
from .stripe_webhook_verifier import StripeWebhookVerifier


class StripeFactory(PaymentProviderFactory):
    def create_authorizer(self) -> Authorizer:
        return StripeAuthorizer()

    def create_refund_processor(self) -> RefundProcessor:
        return StripeRefundProcessor()

    def create_webhook_verifier(self) -> WebhookVerifier:
        return StripeWebhookVerifier()
