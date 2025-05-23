from rest_framework import serializers
from books.models import Review
from users.serializers import UserCardSerializer


class ReviewCardSerializer(serializers.ModelSerializer):
    reviewer = UserCardSerializer()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('reviewer', 'rating', 'comment', 'updated_at',)

    def get_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')


class ReviewSerializer(serializers.ModelSerializer):

    error_msgs = {
        'already_rated' : {
            'error': 'You already submitted a rating to this book'
        }
    }
    class Meta:
        model = Review
        fields = ('rating', 'comment',)

    def validate(self, attrs):
        # If updating review then skip this validation
        if self.instance:
            return attrs
        
        book_id = self.context['view'].kwargs.get('book_id')

        # Check if user already submitted a rating to this book
        if Review.objects.filter(book_id = book_id, reviewer_id = self.context['request'].user.id).exists():
            raise serializers.ValidationError(self.error_msgs['already_rated'])
        
        return attrs

