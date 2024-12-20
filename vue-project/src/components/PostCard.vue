<template>
    <div class="bg-[#2c3e50] border border-[#e74c3c] text-white shadow-lg rounded-lg p-4 flex flex-col w-full h-[45vh] my-4">
        <h3 class="text-xl font-semibold mb-2 break-words">{{ post.text }}</h3>
        <p class="text-sm text-gray-400 mb-1">
            <strong>Author:</strong> {{ post.user.username }}
        </p>
        <p class="text-sm text-gray-400 mb-1">
            <strong>Posted On:</strong> {{ formatDate(post.timestamp) }}
        </p>
        <p class="text-sm text-gray-400">
            <strong>Comments:</strong> {{ post.comments.length }}
        </p>

        <div v-if="post.comments && post.comments.length > 0">
            <h4 class="text-lg font-semibold mt-4">Comments:</h4>
            <ul class="list-disc pl-5">
                <li v-for="comment in post.comments.slice(0, 3)" :key="comment.id" class="mt-2">
                    <p class="text-sm">
                        <strong>{{ comment.user.username }}:</strong> {{ comment.text }}
                    </p>
                    <p class="text-xs text-gray-400">{{ formatDate(comment.timestamp) }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        post: {
            type: Object,
            required: true,
        },
    },
    methods: {
        formatDate(timestamp) {
            const options = { year: "numeric", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" };
            return new Date(timestamp).toLocaleDateString(undefined, options);
        },
    },
};
</script>
