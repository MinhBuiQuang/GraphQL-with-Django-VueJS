<template>
    <div>
        <b-table striped hover :items="allSinhvien"  />
    </div>
</template>

<script>
import gql from 'graphql-tag';
// GraphQL query
const postsQuery = gql`
  query{
  allSinhvien {
    id
    name
    msv
    lop
    ngaysinh
  }
}
`;
export default {
  data: () => ({    
    allSinhvien: [],
    fields: ['msv', 'name'],
    loading: 0,
  }),
  // Apollo GraphQL
  apollo: {
    allSinhvien: {
      query: postsQuery,
      loadingKey: 'loading',
    },
  },
};
</script>

